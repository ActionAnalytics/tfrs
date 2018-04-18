/*
 * Presentational component
 */
import React from 'react';
import PropTypes from 'prop-types';

import Loading from '../../app/components/Loading';

import CreditTransferProgress from './CreditTransferProgress';
import CreditTransferTextRepresentation from './CreditTransferTextRepresentation';
import CreditTransferVisualRepresentation from './CreditTransferVisualRepresentation';
import CreditTransferFormButtons from './CreditTransferFormButtons';
import CreditTransferType from './CreditTransferType';

const CreditTransferDetails = props => (
  <div className="credit-transfer">
    {props.isFetching && <Loading />}
    {!props.isFetching &&
      <div>
        <h1>
          {props.tradeType.id &&
            <CreditTransferType type={props.tradeType.id} />
          }
        </h1>
        <CreditTransferProgress status={props.status} />
        <div className="credit-transfer-details">
          <div className="main-form">
            <CreditTransferTextRepresentation
              creditsFrom={props.creditsFrom}
              creditsTo={props.creditsTo}
              numberOfCredits={props.numberOfCredits}
              status={props.status}
              tradeEffectiveDate={props.tradeEffectiveDate}
              tradeType={props.tradeType}
              totalValue={props.totalValue}
            />
          </div>
        </div>
        <CreditTransferVisualRepresentation
          creditsFrom={props.creditsFrom}
          creditsTo={props.creditsTo}
          numberOfCredits={props.numberOfCredits}
          totalValue={props.totalValue}
        />
        {props.note !== '' &&
          <div className="well transparent">
            <div>Notes: {props.note}</div>
          </div>
        }
        <form onSubmit={e => e.preventDefault()}>
          <CreditTransferFormButtons
            id={props.id}
            changeStatus={props.changeStatus}
            actions={props.buttonActions}
          />
        </form>
      </div>
    }
  </div>
);

CreditTransferDetails.defaultProps = {
  creditsFrom: {
    name: '...'
  },
  creditsTo: {
    name: '...'
  },
  fairMarketValuePerCredit: '0',
  id: 0,
  note: '',
  numberOfCredits: '0',
  status: {
    id: 0,
    status: ''
  },
  totalValue: '0',
  tradeEffectiveDate: '',
  tradeType: {
    theType: 'sell'
  }
};

CreditTransferDetails.propTypes = {
  buttonActions: PropTypes.arrayOf(PropTypes.string).isRequired,
  changeStatus: PropTypes.func.isRequired,
  creditsFrom: PropTypes.shape({
    id: PropTypes.number,
    name: PropTypes.string
  }),
  creditsTo: PropTypes.shape({
    id: PropTypes.number,
    name: PropTypes.string
  }),
  fairMarketValuePerCredit: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number
  ]),
  id: PropTypes.number,
  isFetching: PropTypes.bool.isRequired,
  note: PropTypes.string,
  numberOfCredits: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number
  ]),
  status: PropTypes.shape({
    id: PropTypes.number,
    status: PropTypes.string
  }),
  totalValue: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number
  ]),
  tradeEffectiveDate: PropTypes.string,
  tradeType: PropTypes.shape({
    id: PropTypes.number,
    name: PropTypes.string,
    theType: PropTypes.string
  })
};

export default CreditTransferDetails;
