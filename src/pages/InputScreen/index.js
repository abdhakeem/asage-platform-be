import React, { useState } from 'react'
import {Container, Row, Col } from "react-bootstrap";
import Sidebar from '../../components/sidebar'

import FirstScreen from '../FirstScreen';
import SecondScreen from '../SecondScreen';
import ThirdScreen from '../ThirdScreen';

export default function InputScreen() {

    const mock_material_list = [{
        idx: 1, 
        item: "item", 
        file_source: "fs", 
        scope_category: "scope-category", 
        scope_sub_category: "scope sub category", 
        accepted: true
    },
    {
        idx: 2, 
        item: "item 2", 
        file_source: "fs 2", 
        scope_category: "scope-category", 
        scope_sub_category: "scope sub category", 
        accepted: true
    }]
        
    const [currentPage, setCurrentPage] = useState(2)
    const [fileList, setFileList] = useState([]) 
    const [materialList, setMaterialList] = useState(mock_material_list)

    const moveToNextPage = () => setCurrentPage((page) => page + 1)

    const pages = {
        0: (<FirstScreen onChange={moveToNextPage} />),
        1: (
        <SecondScreen 
        onChange={moveToNextPage} 
        fileList={fileList} 
        onFileListChange={(newFileList) => setFileList(newFileList)}
        materialList={materialList}
        onMaterialListChange={(newMaterialList) => setMaterialList(newMaterialList)}/>),
        2: (
        <ThirdScreen 
        onChange={moveToNextPage} 
        materialList={materialList}
        onMaterialListChange={(newMaterialList) => setMaterialList(newMaterialList)}/>)
    }
    return (
        <>
             <Container fluid>
                <Row>
                    <Col xs={3} id="sidebar-wrapper">      
                      <Sidebar />
                    </Col>
                    <Col xs={9} id="page-content-wrapper">
                        {
                            pages[currentPage]
                        }
                    </Col>
                    </Row>
            </Container>
        </>
    )
}