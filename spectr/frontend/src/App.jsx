import React from "react";
import {Typography, Grid } from '@material-ui/core';
import Paper from '@material-ui/core/Paper'
import Box from '@material-ui/core/Box';

const App = () =>{
    return (
        <Paper 
        container
        elevation="24"
        justifyContent= "center">
        <Box sx={{
            marginTop: 0,
             height: 600,
            borderRadius: "10px",
            backgroundColor: "#151238"
        }}>
            <Grid>
<Typography>lol</Typography>
            </Grid>
        </Box> 
       
        </Paper>

    );

}
export default App;
