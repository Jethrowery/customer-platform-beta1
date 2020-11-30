import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axios';
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

const Search = () => {
	const classes = useStyles();
	const search = 'search';
	const [appState, setAppState] = useState({
		search: '',
		accounts: [],
	});

	useEffect(() => {
		axiosInstance.get(search + '/' + window.location.search).then((res) => {
			const allAccounts = res.data;
			setAppState({ accounts: allAccounts });
			console.log(res.data);
		});
	}, [setAppState]);

	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Grid container spacing={5} alignItems="flex-end">
					{appState.accounts.map((account) => {
						return (
							// Enterprise card is full width at sm breakpoint
							<Grid item key={account.id} xs={12} md={4}>
								<Card className={classes.card}>
									<Link
										color="textPrimary"
										href={'/acccount/' + account.slug}
										className={classes.link}
									>
										<CardMedia
											className={classes.cardMedia}
											image="https://source.unsplash.com/random"
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
											{account.accountname.substr(0, 50)}...
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
export default Search;
