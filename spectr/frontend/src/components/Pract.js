import Grid from '@mui/material/Grid';
import { Typography } from "@mui/material";
import Paper from '@mui/material/Paper';
import DropDown from "./DropDown";
import Box from '@mui/material/Box';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';

const Pract = () => {
    return (
        <Paper sx={{ display: 'flex', flexWrap: 'wrap', padding: '10px' }}>
                  {[...Array(10)].map((_, index) => (

                <Box sx={{ width: '20%', padding: '10px' }}>
<FormControl fullWidth>
            <InputLabel id={`demo-simple-select-label-${index}`}>{`Property ${index + 1}`}</InputLabel>
            <Select
              labelId={`demo-simple-select-label-${index}`}
              id={`demo-simple-select-${index}`}
              label={`Property ${index + 1}`}
              value={''} // TODO: replace with state value
              onChange={() => {}} // TODO: replace with change handler
            >
              {/* TODO: replace field variable and map function with correct options */}
              
            </Select>
          </FormControl>

        </Box>
              ))}

      </Paper>
    )
}

export default Pract;