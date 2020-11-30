import React from 'react';
import ReactDOM from 'react-dom';
import * as serviceWorker from './serviceWorker';
import './index.css';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';
import App from './App';
import Header from './components/header';
import Footer from './components/footer';
import Register from './components/auth/register';
import Login from './components/auth/login';
import Logout from './components/auth/logout';
import Single from './components/Accounts/single';
import Search from './components/Accounts/search';
import Admin from './Admin';
import Adminy from './axiosy';
import YourComponent from './axy_graph';
import Admin01 from './components/adminy/Admin01';
import Admin02 from './components/adminy/Admin02';
import Admin03 from './components/adminy/Admin03';
import Admin04 from './components/adminy/Admin04';
import Admin05 from './components/adminy/Admin05';
import Admin06 from './components/adminy/Admin06';
import Admin07 from './components/adminy/Admin07';
import Admin08 from './components/adminy/Admin08';
import Admin09 from './components/adminy/Admin09';
import Admin10 from './components/adminy/Admin10';
import Admin11 from './components/adminy/Admin11';
import Admin12 from './components/adminy/Admin12';
import Admin13 from './components/adminy/Admin13';
import Admin14 from './components/adminy/Admin14';
import Admin15 from './components/adminy/Admin15';
import Create from './components/admin/create';
import Edit from './components/admin/edit';
import Delete from './components/admin/delete';

const routing = (
	<Router>
		<React.StrictMode>
			<Header />
			<Switch>
				<Route exact path="/graph" component={YourComponent} />
				<Route exact path="/" component={App} />
				<Route exact path="/summary" component={Adminy} />
				<Route exact path="/err01" component={Admin01} />
				<Route exact path="/err02" component={Admin02} />
				<Route exact path="/err03" component={Admin03} />
				<Route exact path="/err04" component={Admin04} />
				<Route exact path="/err05" component={Admin05} />
				<Route exact path="/err06" component={Admin06} />
				<Route exact path="/err07" component={Admin07} />
				<Route exact path="/err08" component={Admin08} />
				<Route exact path="/err09" component={Admin09} />
				<Route exact path="/err10" component={Admin10} />
				<Route exact path="/err11" component={Admin11} />
				<Route exact path="/err12" component={Admin12} />
				<Route exact path="/err13" component={Admin13} />
				<Route exact path="/err14" component={Admin14} />
				<Route exact path="/err15" component={Admin15} />
				<Route exact path="/admin" component={Admin} />

				<Route exact path="/admin/create" component={Create} />
				<Route exact path="/admin/edit/:id" component={Edit} />
				<Route exact path="/admin/delete/:id" component={Delete} />
				<Route path="/register" component={Register} />
				<Route path="/login" component={Login} />
				<Route path="/logout" component={Logout} />
				<Route path="/account/:slug" component={Single} />
				<Route path="/search" component={Search} />
			</Switch>
			<Footer />
		</React.StrictMode>
	</Router>
);

ReactDOM.render(routing, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
