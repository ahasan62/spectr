import { 
    TableContainer,
    Table,
    TableHead,
    TableBody,
    TableRow,
    TableCell,
    Paper,

} from '@mui/material'
import { useEffect, useState } from "react";
import axios from 'axios'
import FileCard from './FileCard';

function FileTable({files})  {
    console.log("from filelist ",files)

    // const [files, setFiles] = useState([]);
    // const getFiles = async () => {
    //     const response = await axios.get('http://localhost:8000/files')
    //     const filenames = response.data
    //     setFiles(filenames)
    // }
    // useEffect(() => {
    //     getFiles();

    // },[])

    return ( <TableContainer component ={Paper}>
        <Table aria-label='simple table' >
            <TableHead>
                <TableRow>
                {/* 'molecule','isocode','linelist','velocity','thermal','profile','temperature','log_columndensity','resolution','fileName','file' */}
                    <TableCell>molecule</TableCell>
                    <TableCell>isocode</TableCell>

                    <TableCell>linelist</TableCell>

                    <TableCell>velocity</TableCell>

                    <TableCell>thermal</TableCell>
                    <TableCell>profile</TableCell>
                    <TableCell>temperature</TableCell>
                    <TableCell>log column density</TableCell>
                    <TableCell>resolution</TableCell>
                    <TableCell align='center'>Download</TableCell>

                </TableRow>
            </TableHead>
            <TableBody>
                {files.map(row => (
                    <TableRow key={row.fileName} sx = {{'&:last-child td, &:last-child th':{border: 0}}}>
                    <TableCell> {row.molecule} </TableCell> 
                    <TableCell> {row.isocode} </TableCell> 
                    <TableCell> {row.linelist} </TableCell> 
                    <TableCell> {row.velocity} </TableCell> 
                    <TableCell> {row.thermal} </TableCell> 
                    <TableCell> {row.profile} </TableCell> 
                    <TableCell> {row.temperature} </TableCell> 
                    <TableCell> {row.log_columndensity} </TableCell> 
                    <TableCell> {row.resolution} </TableCell> 
                    <TableCell align='center'> 
                    <FileCard file={row.fileName} />
                     </TableCell> 

                    </TableRow>
                ))}
            </TableBody>
        </Table>
    </TableContainer>
    );
}
export default FileTable;
