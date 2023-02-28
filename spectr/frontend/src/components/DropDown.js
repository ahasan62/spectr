
import React from 'react';
import axios from 'axios'
import { useEffect, useState } from "react";
import { Typography, Checkbox } from '@mui/material';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Box from '@mui/material/Box';




const DropDown = ({ field, property, onSelect }) => {
    const [fieldname, setField] = React.useState([]);

    const handleChange = (event) => {
      const selectedValue = event.target.value;
      setField(selectedValue);
      onSelect(selectedValue); // pass the selected option to the parent component

      // onSelect(event.target.value);

      };
    return (
    <Box sx={{ display: 'flex', justifyContent: 'space-between', padding: '10px' }}>
      <FormControl sx={{ width: '25%' }} >
      <InputLabel id="demo-simple-select-label">{property}</InputLabel>
      <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          label={property}
          value={fieldname}
          onChange={handleChange}

        >
        {field.map((f) => (
            <MenuItem value={f} key={f.value} >{f}</MenuItem>
        ))}
  

        </Select>

      </FormControl>

        </Box>
)
}

export default DropDown;
