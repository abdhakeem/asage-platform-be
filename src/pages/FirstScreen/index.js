
import {Row, Col } from "react-bootstrap";

import CardOne from "../../assets/cardOne.png"
import CardTwo from "../../assets/cardTwo.png"
import CardThree from "../../assets/cardThree.png"


import styles from './styles.module.scss'

export default function FirstScreen(props) {

    return (
        <>
            <h1 className={"text-start"}>My Emission Activities</h1>

            <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Data Inputs</a></li>
                <li class="breadcrumb-item active" aria-current="page">Select</li>
            </ol>
            </nav>

            <h2>Let our AI-engine do the laborious work for you</h2>
            <h3>How would you like to automate your Scope 1, 2 and 3 data input?</h3>
            <Row>
                <Col xs={4}>
                    <div className={styles.card + " card"}>
                        <div class="card-body">
                            <img src={CardOne} className={styles.cardIcon} />
                            <p className={styles.cardText + " card-text"}>Upload file(s) of any format with data of any amount</p>
                        </div>
                    </div>
                </Col>
                <Col xs={4}>
                    <div>
                        <div className={styles.card + " card"}>
                            <div class="card-body">
                                <img src={CardTwo} className={styles.cardIcon} />
                                <p className={styles.cardText + " card-text"}>Enable AsageAI to automatically identify Scope 1, 2 or 3 data from your workflow software or emails
                                </p>
                            </div>
                        </div>
                        <p className={styles.comingSoon}>Coming Soon!</p>
                    </div>
                </Col>
                <Col xs={4}>
                    <div>
                        <div className={styles.card + " card"}>
                            <div class="card-body">
                                <img src={CardThree} className={styles.cardIcon} />
                                <p className={styles.cardText + " card-text"}>Integrate AsageAI with any of your existing 3rd party data sources
                                </p>
                            </div>
                        </div>
                        <p className={styles.comingSoon}>Coming Soon!</p>
                    </div>
                </Col>
            </Row>
            <button type="button" class="btn btn-secondary btn-lg" onClick={() => props.onChange()}>Next</button>

            <Row>
                Powered by
            </Row>
        </>
    )
}