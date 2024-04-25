
import { useState } from "react"
import {Row, Col } from "react-bootstrap";
import Dropzone from 'react-dropzone'

import CardOne from "../../assets/cardOne.png"
import {useDropzone} from 'react-dropzone'
import { useCallback } from "react";
import Table from 'react-bootstrap/Table';

import styles from './styles.module.scss'

const ProcessDataApi = "http://localhost:8000/process_document/"

export default function SecondScreen(props) {

    const [currentFileId, setCurrentFileId] = useState(1)

    const onDrop = useCallback(async acceptedFiles => {
        const formData = new FormData();
        const currentFile = acceptedFiles[acceptedFiles.length - 1]
        formData.append('file', currentFile);

        try {
            const response = await fetch(ProcessDataApi, {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            props.onFileListChange(
            [...props.fileList, 
                {
                    id: currentFileId,
                    fileName: currentFile.name,
                    format: currentFile.type,
                    uploadStatus: "Uploaded",
                    dataStatus: "Processed",
                }
            ])
            const materialList = data.materials.map((material) => ({ ...material, accepted: true}))
            props.onMaterialListChange([...props.materialList, ...materialList])
            setCurrentFileId(currentFileId => currentFileId + 1)
            console.log('Upload successful:', data);
        } catch (error) {
            console.error('Error uploading file:', error);
        }
      }, [])

      const {getRootProps, getInputProps, isDragActive} = useDropzone({onDrop})


    return (
        <>
            <h1 className={"text-start"}>My Emission Activities</h1>

            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="#">Data Inputs</a></li>
                    <li class="breadcrumb-item active" aria-current="page">Upload your file</li>
                </ol>
            </nav>
            <div className={styles.upperPart}>
                <div {...getRootProps()} className={styles.dragDropArea}>
                    <input {...getInputProps()}/>
                    <div className={styles.dragDropInner}>
                        <img src={CardOne} className={styles.imgCard}/>
                        {isDragActive ? (
                            <p className={styles.dragDropLabel}>
                                Drop here! <br />
                            </p>
                        ) :
                        (
                            <>
                        <p className={styles.dragDropLabel}>
                            Drag-and-drop <br />
                            any file here! <br />
                            <span style={{fontSize: '20px', marginBottom: "32px"}}>OR</span>
                        </p>
                        <button type="button" class="btn btn-secondary btn-lg">Select a file</button>
                        </>)}
                    </div>
                </div>
            </div>
            <div>
                <Table striped bordered>
                <thead>
                    <tr>
                    <th>S/N</th>
                    <th>File name</th>
                    <th>Format</th>
                    <th>Upload Status</th>
                    <th>Data Interpretation Status</th>
                    </tr>
                </thead>
                { props.fileList.map(fileObject => (
                    <tbody>
                    <tr>
                    <td>{fileObject.id}</td>
                    <td>{fileObject.fileName}</td>
                    <td>{fileObject.format}</td>
                    <td>{fileObject.uploadStatus}</td>
                    <td>{fileObject.dataStatus}</td>
                    </tr>
                </tbody>
                ))}
                </Table>
            </div>
            <button type="button" class="btn btn-secondary btn-lg" onClick={() => props.onChange()}>Next</button>
        </>
    )
}