import React, { useEffect, useState } from 'react';
import './App.css';
//import logo from './logo.svg';
import Accounts from './components/Accounts/accounts';
import AccountsLoadingComponent from './components/Accounts/accountsLoading';
import axiosInstance from './axios';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
//
//export default App;

function App() {
	const AccountsLoading = AccountsLoadingComponent(Accounts);
	const [appState, setAppState] = useState({
		loading: true,
		accounts: null,
	});

	useEffect(() => {
		axiosInstance.get().then((res) => {
			const allAccounts = res.data;
			console.log(res.data);
			setAppState({ loading: false, accounts: allAccounts });
			console.log(res.data);
		});
	}, [setAppState]);
	return (
		<div className="App">
			<h1 className = "Appy">Welcome to your company's compliance platform.</h1>
			<AccountsLoading isLoading={appState.loading} accounts={appState.accounts} />
			
		</div>
	);

	return (
		<a className="App-link"
		href="https://aceallizon.com/"
		target="_blank"
		rel="noopener noreferrer"
		></a>
	)
}
export default App;
