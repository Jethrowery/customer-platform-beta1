import React, { useEffect, useState } from 'react';
import './App.css';
import Accounts from './components/admin/accounts';
import AccountsLoadingComponent from './components/Accounts/accountsLoading';
import axiosInstance from './axios';

function Admin() {
	const AccountsLoading = AccountsLoadingComponent(Accounts);
	const [appState, setAppState] = useState({
		loading: true,
		accounts: null,
	});

	useEffect(() => {
		axiosInstance.get(`platform/`).then((res) => {
			const allAccounts = res.data;
			setAppState({ loading: false, accounts: allAccounts });
			console.log(res.data);
		}
		
		);
	}, [setAppState]);

	return (
		<div className="App">
			<h1>Exceptions Identified</h1>
			<AccountsLoading isLoading={appState.loading} accounts={appState.accounts} />
		</div>
	);
}
export default Admin;
