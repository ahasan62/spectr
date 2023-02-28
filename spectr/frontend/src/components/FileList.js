import FileCard from './FileCard';

const FileList = ({ files }) => {
    console.log("from filelist ",files)
    return (
        <div>
            {files.map((file) => (
                <FileCard file={file} key={file.id} />
            ))}
        </div>
    )
}

export default FileList;