import axios from 'axios';
import React, { useEffect, useState } from 'react';
import './Appy.css';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Button from '@material-ui/core/Button';
import Trend from 'react-trend';

const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '56.25%', // 16:9
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},
	accountTitle: {
		fontSize: '50px',
		textAlign: 'left',
	},
	accountText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '32px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));

const baseURL = 'https://dashboard.heroku.com/apps/customer-platform-beta1/api/';

const axiosy = axios.create({
	baseURL: baseURL,
	timeout: 5000,
	headers: {
		Authorization: localStorage.getItem('access_token')
			? 'JWT ' + localStorage.getItem('access_token')
			: null,
		'Content-Type': 'application/json',
		accept: 'application/json',
	},
});

const YourComponent = () => (
	<Trend
		smooth
		autoDraw
		autoDrawDuration={3000}
		autoDrawEasing="ease-out"
		data={[0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0]}
		gradient={['#00c6ff', '#F0F', '#FF0']}
		radius={8.9}
		strokeWidth={1.1}
		strokeLinecap={'square'}
	/>
);

function Adminy() {
	const classes = useStyles();
	
	const [bccState, setBccState] = useState({ loading: true, bccerr: [], });
	const [beiState, setBeiState] = useState({ loading: true, beierr: [], });
	const [bmiState, setBmiState] = useState({ loading: true, bmierr: [], });
	const [ccyState, setCcyState] = useState({ loading: true, ccyerr: [], });
	const [isinState, setIsinState] = useState({ loading: true, isinerr: [], });
	const [mexpiryState, setMexpiryState] = useState({ loading: true, mexpiryerr: [], });
	const [iexpiryState, setIexpiryState] = useState({ loading: true, iexpiryerr: [], });
	const [imaturityState, setImaturityState] = useState({ loading: true, imaturityerr: [], });
	const [transmitState, setTransmitState] = useState({ loading: true, transmiterr: [], });
	const [instmtexpiryState, setInstmtexpiryState] = useState({ loading: true, instmtexpiryerr: [], });
	const [iinstmtexpiryState, setIinstmtexpiryState] = useState({ loading: true, iinstmtexpiryerr: [], });
	const [idiState, setIdiState] = useState({ loading: true, idierr: [], });
	const [reviewdateState, setReviewdateState] = useState({ loading: true, reviewdateerr: [], });
	const [netamtState, setNetamtState] = useState({ loading: true, netamterr: [], });
	const [missingbondState, setMissingbondState] = useState({ loading: true, missingbonderr: [], });

	useEffect(() => {
		axiosy.get(`platform/errd_bcc/`).then((res) => { setBccState({ loading: true, bccerr: res.data }); });
		axiosy.get(`platform/errd_bei/`).then((res) => { setBeiState({ loading: true, beierr: res.data }); });
		axiosy.get(`platform/errd_bmi/`).then((res) => { setBmiState({ loading: true, bmierr: res.data }); });
		axiosy.get(`platform/errd_cc/`).then((res) => { setCcyState({ loading: true, ccyerr: res.data }); });
		axiosy.get(`platform/errd_isin/`).then((res) => { setIsinState({ loading: true, isinerr: res.data }); });
		axiosy.get(`platform/errd_mexpiry/`).then((res) => { setMexpiryState({ loading: true, mexpiryerr: res.data }); });
		axiosy.get(`platform/errd_iexpiry/`).then((res) => { setIexpiryState({ loading: true, iexpiryerr: res.data }); });
		axiosy.get(`platform/errd_imaturity/`).then((res) => { setImaturityState({ loading: true, imaturityerr: res.data }); });
		axiosy.get(`platform/errd_transmit/`).then((res) => { setTransmitState({ loading: true, transmiterr: res.data }); });
		axiosy.get(`platform/errd_instmtexpiry/`).then((res) => { setInstmtexpiryState({ loading: true, instmtexpiryerr: res.data }); });
		axiosy.get(`platform/errd_iinstmtexpiry/`).then((res) => { setIinstmtexpiryState({ loading: true, iinstmtexpiryerr: res.data }); });
		axiosy.get(`platform/errd_idi/`).then((res) => { setIdiState({ loading: true, idierr: res.data }); });
		axiosy.get(`platform/errd_reviewdate/`).then((res) => { setReviewdateState({ loading: true, reviewdateerr: res.data }); });
		axiosy.get(`platform/errd_netamt/`).then((res) => { setNetamtState({ loading: true, netamterr: res.data }); });
		axiosy.get(`platform/errd_missingbond/`).then((res) => {setMissingbondState({ loading: true, missingbonderr: res.data });});
	},
		
		[setBccState, setBeiState, setBmiState, setCcyState, setIsinState, setMexpiryState, setIexpiryState, setImaturityState,
			setTransmitState, setInstmtexpiryState, setIinstmtexpiryState, setIdiState, setReviewdateState, setNetamtState, setMissingbondState,]);
	
	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Paper className={classes.root}>
					<TableContainer className={classes.container}>
						<div className="Appy">Summary of Exceptions </div>
						<div class="vertical-center" position="absolute">
							<Button href={'/graph'} variant="contained" color="primary">
								View the trend line
							</Button>
						</div>
						<Table stickyHeader aria-label="sticky table">
							<TableHead>
								<TableRow>
									<TableCell align="left">Description</TableCell>
									<TableCell align="right">Number of exceptions</TableCell>
								</TableRow>
							</TableHead>
							<TableBody>
								<TableRow>
									<TableCell component="th" scope="row">
										Buyer Country Code is invalid
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err01'}
											className={classes.link}
											>
											{bccState.bccerr.length}
										</Link>
									</TableCell>
								</TableRow>

								<TableRow>
									<TableCell component="th" scope="row">
										Buyer Entity Identifier is invalid
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err02'}
											className={classes.link}
											>
											{beiState.beierr.length}
										</Link>
									</TableCell>
								</TableRow>

								<TableRow>
									<TableCell component="th" scope="row">
										Buyer Market Identifier was not found
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err03'}
											className={classes.link}
											>
											{bmiState.bmierr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Currency Code is invalid
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err04'}
											className={classes.link}
											>
											{ccyState.ccyerr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Invalid ISIN
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err05'}
											className={classes.link}
											>
											{isinState.isinerr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Expiry date is missing
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err06'}
											className={classes.link}
											>
											{mexpiryState.mexpiryerr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Expiry date is invalid
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err07'}
											className={classes.link}
											>
											{iexpiryState.iexpiryerr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Maturity date is N/A to Instrument
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err08'}
											className={classes.link}
											>
											{imaturityState.imaturityerr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Transmitting ID code for the buyer invalid  
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err09'}
											className={classes.link}
											>
											{transmitState.transmiterr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Investment decision identifier is missing 
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err12'}
											className={classes.link}
											>
											{idiState.idierr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Product review date error
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err13'}
											className={classes.link}
											>
											{reviewdateState.reviewdateerr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Bond type is missing
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err15'}
											className={classes.link}
											>
											{missingbondState.missingbonderr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Net outstanding amount is invalid
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err14'}
											className={classes.link}
											>
											{netamtState.netamterr.length}
										</Link>
									</TableCell>
								</TableRow>
								
								<TableRow>
									<TableCell component="th" scope="row">
										Instrument expiry date is invalid
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err11'}
											className={classes.link}
											>
											{iinstmtexpiryState.iinstmtexpiryerr.length}
										</Link>
									</TableCell>
								</TableRow>

								<TableRow>
									<TableCell component="th" scope="row">
										Instrument expiry date is missing
									</TableCell>
									<TableCell align="right">
										<Link
											color="textPrimary"
											href={'/err10'}
											className={classes.link}
											>
											{instmtexpiryState.instmtexpiryerr.length}
										</Link>
									</TableCell>
								</TableRow>
								
							</TableBody>
						</Table>
					</TableContainer>
				</Paper>
			</Container>
			<div>
				{YourComponent.plot}	
			</div>
		</React.Fragment>
	);
	
}



export default Adminy;
