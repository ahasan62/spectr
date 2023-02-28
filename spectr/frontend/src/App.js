import React from 'react';
import ParamList from './components/ParamList';
import axios from 'axios'
import { useEffect, useState } from "react";
import { Typography } from '@mui/material';
import FileTable from './components/FileTable'

function App() {
  const [files, setFiles] = useState([]);
  const [uniqueMolecule, setUniqueMolecule] = React.useState([]);
  const [uniqueIsocode, setUniqueIsocode] = React.useState([]);
  const [uniqueVelocity, setUniqueVelocity] = React.useState([]);
  const [uniqueTemp, setTemp] = React.useState([]);
  const [uniqueLog, setUniquelogs] = React.useState([]);
  const [downloadFiles, setDownloadFiles] = React.useState([]);

  const getFiles = async () => {
    const response = await axios.get("http://localhost:8000/files")
    console.log(response)
    const filenames = response.data; 
    setFiles(filenames)
    setUniqueMolecule([...new Set(filenames.map(item => item.molecule))])
    setUniqueIsocode([...new Set(filenames.map(item => item.isocode))])
    setUniqueVelocity([...new Set(filenames.map(item => item.velocity))])
    setTemp([...new Set(filenames.map(item => item.temperature))])
    setUniquelogs([...new Set(filenames.map(item => item.log_columndensity))])


  }


  useEffect(() => {
    getFiles();
  },[])
  const searchFileByParam= async (values) => {
    const filteredFiles = files.filter(file => {
      if (parseFloat(file.temperature) < parseFloat(values.temperature1) ||
          parseFloat(file.temperature) > parseFloat(values.temperature2)) {
        return false;
      }
      if (parseFloat(file.log_columndensity) < parseFloat(values.log1) ||
          parseFloat(file.log_columndensity) > parseFloat(values.log2)) {
        return false;
      }
      if (values.molecule && file.molecule !== values.molecule) {
        return false;
      }
      if (values.isocode && file.isocode !== values.isocode) {
        return false;
      }
      if (values.linelist && file.linelist !== values.linelist) {
        return false;
      }
      if (values.velocity && file.velocity !== values.velocity) {
        return false;
      }
      if (values.profile && file.profile !== values.profile) {
        return false;
      }
      if (values.resolution && file.resolution !== values.resolution) {
        return false;
      }
      return true;
    });
  
    console.log("Filtered files:", filteredFiles);
    setDownloadFiles(filteredFiles)
  };
  
 
  

  //  const handleSearch = () => {
  //   // Perform search with selectedFields
  //   console.log("Performing search with", selectedFields);
  // };

  return (
    <div>
      <Typography>SpectraFactory</Typography>
      <ParamList onSearch={searchFileByParam} uniqueMolecule={uniqueMolecule} uniqueIsocode={uniqueIsocode} uniqueVelocity={uniqueVelocity} uniqueTemp={uniqueTemp} uniqueLog={uniqueLog} />
      
      {/* <FileTable files={files} /> */}
      {downloadFiles.length >= 1 ? <FileTable files={downloadFiles} /> : null}

      </div>
  );
}

export default App;