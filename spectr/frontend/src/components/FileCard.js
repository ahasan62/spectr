import React from 'react';
import axios from 'axios';
const FileCard = ({ file }) => {
    const handleDownload = () => {
        axios.get(`http://localhost:8000/download/${file + '.gz'}`, {
            responseType: 'blob',
        }).then((response) => {
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', file);
            document.body.appendChild(link);
            link.click();
        });
    }

    return (
        <div className="card">
            <div className="card-body">
                <button className="btn btn-primary"onClick={handleDownload} >Download</button>
            </div>
        </div>
    );
}

export default FileCard;