import React from 'react';
import Trend from 'react-trend';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';



const YourComponent = () => (
  [
    <Container maxWidth="md" component="main" text-align="center" font-weight="bolder"
      font-size="largest">
      <h1>Visualisation of Exceptions Trend</h1>
    </Container>,
    <Trend
    smooth
    autoDraw
    autoDrawDuration={3000}
    autoDrawEasing="ease-out"
    data={[13,5,13,11,340,285,90,55,2,11,300,193,223,6,10]}
    gradient={['#00c6ff', '#F0F', '#FF0']}
    radius={8.9}
    strokeWidth={1.1}
    strokeLinecap={'square'}
  />,
  
  <Button href={'/summary'} variant="contained" color="primary" class="center">
    Back to summary
  </Button>

  ]
);

export default YourComponent;