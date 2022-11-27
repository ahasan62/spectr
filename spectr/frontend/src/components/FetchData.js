import React, {useState, useEffect} from 'react';
import axios from 'axios';

function FetchData() {

    const [norm, setNorm] = useState([])

    useEffect(() => {
        axios.get("http://localhost:8000/normalized")
        .then(resp => {
            setNorm(resp.data)
            console.log("data is",resp.data)
            console.log("norm is",norm)
            // console.log("length of string",norm[0].normalized.length)
            // console.log("norm molecule is",norm[0].normalized)


        })    
        .catch(error => console.log(error.response.data))

    },[])
    return  (
        <div>
            <p>Data: {norm[0].molecule}</p>


        {/* <h3>{norm[0].normalized}</h3> */}
    </div>
    )
}
export default FetchData;