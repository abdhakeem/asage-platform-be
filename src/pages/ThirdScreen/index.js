
import { useState } from "react"
import {Row, Col, ToggleButtonGroup } from "react-bootstrap";
import Form from 'react-bootstrap/Form';

import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton';

import Table from 'react-bootstrap/Table';

import styles from './styles.module.scss'

const ProcessDataApi = "http://localhost:8000/process_document/"

export default function ThirdScreen(props) {
    return (
        <>
            <h1 className={"text-start"}>My Emission Activities</h1>

            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="#">Data Inputs</a></li>
                    <li class="breadcrumb-item"><a href="#">Upload your file (s)</a></li>
                    <li class="breadcrumb-item active" aria-current="page">Data Validation</li>
                </ol>
            </nav>
            <div>
                <Table striped bordered>
                <thead>
                    <tr>
                    <th>S/N</th>
                    <th>Item</th>
                    <th>File Source</th>
                    <th>Scope Category</th>
                    <th>Scope Sub-Category</th>
                    <th>Accept?</th>
                    </tr>
                </thead>
                { props.materialList.map((material, material_idx) => (
                    <tbody>
                    <tr>
                        
                        <td>{material_idx}</td>
                        <td>{material.item}</td>
                        <td>{material.file_source}</td>
                        <td>{material.scope_category}</td>
                        <td>{material.scope_sub_category}</td>
                        <td>
                            <ButtonGroup>
                                {['No', 'Yes'].map((buttonName, buttonIdx) => (
                                    <ToggleButton
                                        key={`${material_idx}-${buttonIdx}`}
                                        id={`radio-${material_idx}-${buttonIdx}`}
                                        type="radio"
                                        variant={buttonIdx % 2 ? 'outline-success' : 'outline-danger'}
                                        name={`radio-${material_idx}`}
                                        value={buttonName}
                                        checked={(material.accepted && buttonName === "Yes") ||  (!material.accepted && buttonName === "No")}
                                        onChange={(e) => {
                                            const copyOfMaterialList = [...props.materialList]
                                            copyOfMaterialList[material_idx].accepted = e.currentTarget.value === "Yes"
                                            props.onMaterialListChange(copyOfMaterialList)
                                        }}
                                    >
                                        {buttonName}
                                    </ToggleButton>
                                ))}
                            </ButtonGroup>
                        </td>
                    </tr>
                </tbody>
                ))}
                </Table>
            </div>
            <button type="button" class="btn btn-secondary btn-lg" onClick={() => props.onChange()}>Next</button>
        </>
    )
}