
import React from 'react'
import AsageLogo from "../../assets/logo.svg"
import SliderIcon from "../../assets/sliderIcon.png"
import BarIcon from "../../assets/barIcon.png"
import ChatIcon from "../../assets/chatIcon.png"
import NetZeroIcon from "../../assets/downwardTrend.png"
import WorldIcon from "../../assets/worldIcon.png"
import BuildingIcon from "../../assets/buildingIcon.png"
import DataManagement from "../../assets/dataIcon.png"
import styles from './sidebar.module.scss'
import Stack from 'react-bootstrap/Stack';
import { useState } from 'react'
import { Col, Container, Row } from 'react-bootstrap'


export default function Sidebar() {

    const [ selectedTabIndex, setSelectedTabIndex ] = useState(1)
    const menuItems = () => {
        const menuItems = [
            { name: "Boundary Setting", icon: SliderIcon, active:false},
            { name: "Inputs", icon: BarIcon, active: true},
            { name: "My Dashboard", icon: WorldIcon, active: false},
            { name: "My Consultants", icon: ChatIcon, active: false},
            { name: "Net-Zero Marketplace", icon: NetZeroIcon, active: false},
            { name: "Green Finance Marketplace", icon: BuildingIcon, active: false},
            { name: "Data Management", icon: DataManagement, active: false},
        ]
        return menuItems.map((tab, index) => (
            <li className={index === selectedTabIndex ? styles.listItem + " active" : styles.listItem} onClick={() => setSelectedTabIndex(index)}>
                <Container>
                    <Row>
                        <Col xs={2}>
                            <img src={tab.icon} className={styles.menuIcon}/>
                        </Col>
                        <Col xs={10} className={index === selectedTabIndex ? styles.tabLabel + " active" : styles.tabLabel}>
                            {tab.name}
                        </Col>
                    </Row>
                </Container>
            </li>
        ))
    }
    return (
        <Stack className={styles.sidebarWrapper}>
            <div className={styles.asageLogo}>
                <img src={AsageLogo} />
            </div>
            <div className={styles.asageLogo}>
                Welcome, Aluminium Company X!
            </div>
            <ul className={styles.unorderedList}>
                {menuItems()}
            </ul>
        </Stack>
        
    )
}