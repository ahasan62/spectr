import DropDown from "./DropDown";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useEffect, useState } from "react";

const ParamList = ({onSearch, uniqueMolecule, uniqueIsocode, uniqueVelocity, uniqueTemp, uniqueLog}) => {
    const [values, setValues] = useState({});
    const [isValid, setIsValid] = useState(false);

    const handleSubmit = () => {
        const isValid = validateValues(values);
        console.log(isValid)
        if (isValid){
            
        if (values.temperature1 && values.temperature2 && values.log1 && values.log2) {
            console.log(values)
            onSearch(values)
        
        }
        }
    }
    const validateValues = () => {
         const regex = /^\d*\.?\d{0,2}$/; // allow decimal numbers with up to 2 decimal places
        // only allow numbers

        if (
          regex.test(values.temperature1) &&
          regex.test(values.temperature2) &&
          regex.test(values.log1) &&
          regex.test(values.log2) &&
          Object.keys(values).length === 10 &&
          (parseFloat(values.temperature2) >= parseFloat(values.temperature1)) && (parseFloat(values.log2) >= parseFloat(values.log1))

        ) 

        
        {
            return true
        } else {
            return false
        }
      };
      const handleMoleculeSelect = (selectedMolecule) => {
        setValues((prevState) => ({
            ...prevState,
            molecule: selectedMolecule,
          }));
      }
      const handleIsocodeSelect = (selectedIsocode) => {
        setValues((prevState) => ({
            ...prevState,
            isocode: selectedIsocode,
          }));
      }
      const handleLinelistSelect = (selectedlinelist) => {
        setValues((prevState) => ({
            ...prevState,
            linelist: selectedlinelist,
          }));
      }
      const handleVelocitySelect = (selectedVelocity) => {
        setValues((prevState) => ({
            ...prevState,
            velocity: selectedVelocity,
          }));
      }
      const handleProfileSelect = (selectedProfile) => {
        setValues((prevState) => ({
            ...prevState,
            profile: selectedProfile,
          }));
      }
      const handleResSelect = (selectedRes) => {
        setValues((prevState) => ({
            ...prevState,
            resolution: selectedRes,
          }));
      }
    return (
        <div>
      <DropDown 
      property={'Molecule'} 
      field={uniqueMolecule}
      onSelect={handleMoleculeSelect}

      />
      <DropDown 
      property={'IsoCode'} 
      field={uniqueIsocode} 
      onSelect={handleIsocodeSelect}

      /> 
      <DropDown property={'LineList'} 
      field={['CDSD','HITRAN04']}
      onSelect={handleLinelistSelect}

      />

      <DropDown property={'Velocity'} 
      field={uniqueVelocity}
      onSelect={handleVelocitySelect}

      />
      <DropDown property={'Profile'} 
      field={['gauss']}
      onSelect={handleProfileSelect}


      />
       <Box
      component="form"
      sx={{width: '25%' }}
      noValidate
      autoComplete="off"
    >
      <TextField 
      id="outlined-basic" 
      label="Temperature1 K" 
      variant="outlined" 
      value={values.temperature1}
      onChange={(e) =>
        setValues({ ...values, temperature1: e.target.value })
      }
      /> 
      <TextField 
      id="outlined-basic" 
      label="Temperature2 K" 
      variant="outlined" 
      value={values.temperature2}
      onChange={(e) =>
        setValues({ ...values, temperature2: e.target.value })
      }
      />

    </Box>
    <Box
      component="form"
      sx={{width: '25%' }}
      noValidate
      autoComplete="off"
    >
      <TextField 
      id="outlined-basic" 
      label="Log1" 
      variant="outlined" 
      value={values.log1}
      onChange={(e) =>
        setValues({ ...values, log1: e.target.value })
      }
      /> 
      <TextField 
      id="outlined-basic" 
      label="Log2" 
      variant="outlined" 
      value={values.log2}
      onChange={(e) =>
        setValues({ ...values, log2: e.target.value })
      }
      />

    </Box>
    

      <DropDown property={'Resolution'} 
      field={['R600.00','R65000.00']}
      onSelect={handleResSelect}


      />
    <Button onClick={handleSubmit}>Search</Button>



        </div>
    )
}


export default ParamList;