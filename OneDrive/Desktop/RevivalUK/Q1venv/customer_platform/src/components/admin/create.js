import React, { useState } from 'react';
import axiosInstance from '../../axios';
import { useHistory } from 'react-router-dom';
//MaterialUI
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import IconButton from '@material-ui/core/IconButton';
import PhotoCamera from '@material-ui/icons/PhotoCamera';

const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main,
	},
	form: {
		width: '100%', // Fix IE 11 issue.
		marginTop: theme.spacing(3),
	},
	submit: {
		margin: theme.spacing(3, 0, 2),
	},
}));

export default function Create() {
	//https://gist.github.com/hagemann/382adfc57adbd5af078dc93feef01fe1
	function slugify(string) {
		const a =
			'àáâäæãåāăąçćčđďèéêëēėęěğǵḧîïíīįìłḿñńǹňôöòóœøōõőṕŕřßśšşșťțûüùúūǘůűųẃẍÿýžźż·/_,:;';
		const b =
			'aaaaaaaaaacccddeeeeeeeegghiiiiiilmnnnnoooooooooprrsssssttuuuuuuuuuwxyyzzz------';
		const p = new RegExp(a.split('').join('|'), 'g');

		return string
			.toString()
			.toLowerCase()
			.replace(/\s+/g, '-') // Replace spaces with -
			.replace(p, (c) => b.charAt(a.indexOf(c))) // Replace special characters
			.replace(/&/g, '-and-') // Replace & with 'and'
			.replace(/[^\w\-]+/g, '') // Remove all non-word characters
			.replace(/\-\-+/g, '-') // Replace multiple - with single -
			.replace(/^-+/, '') // Trim - from start of text
			.replace(/-+$/, ''); // Trim - from end of text
	}
	//

	const history = useHistory();
	const initialFormData = Object.freeze({
		title: '',
		slug: '',
		excerpt: '',
		content: '',
	});

	const [accountData, updateFormData] = useState(initialFormData);
	const [accountimage, setAccountImage] = useState(null);

	const handleChange = (e) => {
		if ([e.target.name] == 'image') {
			setAccountImage({
				image: e.target.files,
			});
			console.log(e.target.files);
		}
		if ([e.target.name] == 'title') {
			updateFormData({
				...accountData,
				[e.target.name]: e.target.value.trim(),
				['slug']: slugify(e.target.value.trim()),
			});
		} else {
			updateFormData({
				...accountData,
				[e.target.name]: e.target.value.trim(),
			});
		}
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		let formData = new FormData();
		formData.append('entityname', accountData.entityname);
		formData.append('slug', accountData.slug);
		formData.append('accountname', accountData.accountname);
		formData.append('accountno', accountData.accountno);
		formData.append('content', accountData.content);
		formData.append('amount', accountData.amount);
		axiosInstance.account(`platform/admin/create/`, formData);
		history.push({
			pathname: '/admin/',
		});
		window.location.reload();
	};

	// const config = { headers: { 'Content-Type': 'multipart/form-data' } };
	// const URL = 'http://127.0.0.1:8000/api/admin/creats/';
	// let formData = new FormData();
	// formData.append('title', accountData.title);
	// formData.append('slug', accountData.slug);
	// formData.append('author', 1);
	// formData.append('excerpt', accountData.excerpt);
	// formData.append('content', accountData.content);
	// formData.append('image', accountimage.image[0]);
	// axios
	// 	.account(URL, formData, config)
	// 	.then((res) => {
	// 		console.log(res.data);
	// 	})
	// 	.catch((err) => console.log(err));

	const classes = useStyles();

	return (
		<Container component="main" maxWidth="xs">
			<CssBaseline />
			<div className={classes.paper}>
				<Avatar className={classes.avatar}></Avatar>
				<Typography component="h1" variant="h5">
					Create New Account
				</Typography>
				<form className={classes.form} noValidate>
					<Grid container spacing={2}>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="number"
								label="Account Number"
								name="number"
								autoComplete="number"
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="excerpt"
								label="Account Name"
								name="name"
								autoComplete="name"
								onChange={handleChange}
								multiline
								rows={4}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="slug"
								label="slug"
								name="slug"
								autoComplete="slug"
								value={accountData.slug}
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="amount"
								label="amount"
								name="amount"
								autoComplete="amount"
								onChange={handleChange}
								multiline
								rows={4}
							/>
						</Grid>
						<input
							accept="image/*"
							className={classes.input}
							id="amount-image"
							onChange={handleChange}
							name="image"
							type="file"
						/>
					</Grid>
					<Button
						type="submit"
						fullWidth
						variant="contained"
						color="primary"
						className={classes.submit}
						onClick={handleSubmit}
					>
						Create Account
					</Button>
				</form>
			</div>
		</Container>
	);
}
