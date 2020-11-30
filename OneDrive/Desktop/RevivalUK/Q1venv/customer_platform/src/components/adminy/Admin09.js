import React, { useEffect, useState } from 'react';
import './Appy.css';
import Accounts from '../admin/accounts';
import AccountsLoadingComponent from '../Accounts/accountsLoading';
import axiosInstance from '../../axios';

function Admin09() {
	const AccountsLoading = AccountsLoadingComponent(Accounts);
	const [appState, setAppState] = useState({
		loading: true,
		accounts: null,
	});

	useEffect(() => {
		axiosInstance.get(`platform/errd_transmit/`).then((res) => {
			const allAccounts = res.data;
			setAppState({ loading: false, accounts: allAccounts });
			console.log(res.data);
		}
		
		);
	}, [setAppState]);

	return (
		<div className="App">
			<h1>Buyer Transmitting ID Code Exceptions Identified</h1>
			<AccountsLoading isLoading={appState.loading} accounts={appState.accounts} />
		</div>
	);
}
export default Admin09;
