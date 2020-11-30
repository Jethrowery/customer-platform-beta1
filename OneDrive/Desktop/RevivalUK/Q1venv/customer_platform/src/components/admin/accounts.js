import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Button from '@material-ui/core/Button';

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
		fontSize: '16px',
		textAlign: 'left',
	},
	accountText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));

const Accounts = (props) => {
	const { accounts } = props;
	const classes = useStyles();
	if (!accounts || accounts.length === 0) return <p>We apologise, we could not identify any active accounts. Make sure accounts exist in your Frameworks portfolio.</p>;
	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Paper className={classes.root}>
					<TableContainer className={classes.container}>
						<Table stickyHeader aria-label="sticky table">
							<TableHead>
								<TableRow>
									<TableCell colSpan={4} align="right">
										<Button
											href={'/admin/edit'}
											variant="contained"
											color="primary"
										>
											Add comment
										</Button>
									</TableCell>
								</TableRow>
								<TableRow>
									<TableCell>Id</TableCell>
									<TableCell align="left">ISIN</TableCell>
									<TableCell align="left">Country</TableCell>
									<TableCell align="left">Buyer LE ID</TableCell>
									<TableCell align="left">Buyer</TableCell>
									<TableCell align="left">Currency</TableCell>
									<TableCell align="left">Expiry Date</TableCell>
									<TableCell align="left">Value Date</TableCell>
									<TableCell align="left">Fin. Instrument Class</TableCell>
									<TableCell align="left">Investment Decision ID</TableCell>
									<TableCell align="left">Bond Type</TableCell>
									<TableCell align="left">Maturity date</TableCell>
									<TableCell align="left">Review date</TableCell>
									<TableCell align="left">Net Amount ($)</TableCell>
								</TableRow>
							</TableHead>
							<TableBody>
								
								{accounts.map((account) => {
									return (
										<TableRow>
											<TableCell component="th" scope="row">{account.id}</TableCell>
											<TableCell align="left">{account.isin_code}</TableCell>
											<TableCell align="left">{account.buyer_country_code}</TableCell>
											<TableCell align="left">{account.buyer_legal_entity_identifier}</TableCell>
											<TableCell align="left">{account.buyer_market_identifier_code}</TableCell>
											<TableCell align="left">{account.currency_code}</TableCell>
											<TableCell align="left">{account.lia_date}</TableCell>
											<TableCell align="left">{account.lrc_date}</TableCell>
											<TableCell align="left">{account.classification_of_financial_instruments}</TableCell>
											<TableCell align="left">{account.investment_decision_identifier}</TableCell>
											<TableCell align="left">{account.bond_type}</TableCell>
											<TableCell align="left">{account.maturity_date}</TableCell>
											<TableCell align="left">{account.review_date}</TableCell>
											<TableCell align="right">{account.net_position}</TableCell>
										</TableRow>
									);
								})}
								
							</TableBody>
						</Table>
					</TableContainer>
				</Paper>
			</Container>
		</React.Fragment>
	);
};
export default Accounts;
