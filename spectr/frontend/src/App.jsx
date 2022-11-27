import React from "react";
import {Typography, Grid } from '@material-ui/core';
import Paper from '@material-ui/core/Paper'
import Box from '@material-ui/core/Box';
import { useState } from 'react';
import { useEffect } from "react";
// import WavelengthField from "./components/WavelengthField"
// import Hello from "./components/Hello"
import './App.css'
// import MyClass from './components/MyClass';
import Counter from './components/Counter'
import FetchData from "./components/FetchData";

// import FunComponent from "./components/FunComponent";
function App() {
    return (
        <div className="container">
            <h1>Hello React Application</h1>
            <FetchData/>
        </div>
        );
      }
      export default App;
// const App = () =>{
//     const [x1,setx1] = useState(0);
//     const [x2,setx2] = useState(0.35);
//     const [y1,sety1] = useState(0)
//         useEffect(() => {
//             const fetchData = async () => { 
//                const result = await fetch("http://localhost:8000/normalized")
//                const jsonResult = result.json();
//                console.log(jsonResult)

//                sety1(jsonResult)

//             }

//             fetchData()

//     }, [])


//     const changex1 = event => {
//         setx1(event.target.value)
//     }
//     const changex2 = event => {
//         setx2(event.target.value)
//     }
    
    
//     return (
//         <div style={{}}>
//         <Typography style={{marginBottom: "10px"}}>Enter wavelength values</Typography> 

//         <div style={{paddingBottom:"10px"}}>
//         <input
        
//         onChange={changex1}
//         value = {x1}
//         />
//         </div>
//         <div>
//         <input 
//         onChange={changex2}
//         value = {x2}
//         style={{marginRight: "50px"}}
//         />
//         <button onClick ={useEffect}> Enter Data</button>

//         </div>
//         </div>
        
//     );


// }

// export default App;
