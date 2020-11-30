import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';

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
				<Grid container spacing={5} alignItems="flex-end">
					{accounts.map((account) => {
						return (
							// Enterprise card is full width at sm breakpoint
							<Grid item key={account.id} xs={12} md={4}>
								<Card className={classes.card}>
									<Link
										color="textPrimary"
										href={'account/' + account.slug}
										className={classes.link}
									>
										<CardMedia
											className={classes.cardMedia}
											image={account.image}
											title="Image title"
										/>
									</Link>
									<CardContent className={classes.cardContent}>
										<Typography
											gutterBottom
											variant="h6"
											component="h2"
											className={classes.accountTitle}
										>
											{account.name.substr(0, 50)}...
										</Typography>
										{/* <div className={classes.accountText}>
											<Typography color="textSecondary">
												{account.excerpt.substr(0, 40)}...
											</Typography>
										</div> */}
									</CardContent>
								</Card>
							</Grid>
						);
					})}
				</Grid>
			</Container>
		</React.Fragment>
	);
};
export default Accounts;
