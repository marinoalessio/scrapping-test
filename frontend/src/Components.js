import 'bootstrap/dist/css/bootstrap.min.css';
import { Alert, InputGroup, FormControl, Button, Form, ListGroup, Col, Row, Container } from 'react-bootstrap';
import { useState } from 'react';
import API from './API';

function Searchbar(props) {

    const [query, setQuery] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [showAlert, setShowAlert] = useState(false);

    const parseQuery = () => {
        if (/\d/.test(query)) {
            setErrorMessage("The input contains a number!");
            setShowAlert(true);
            return false;
        }

        // you can do other checkings in this section ...

        return true; // true means that everything is okay
    }

    const search = async (input) => {
        try {
            const response = await API.scrapeBoats(input);

            if (response.status === "success") {
                props.setBoatsList(response.boats);
                props.setLoadingList(false);    // this implies that now the list can be shown
            }
            else if (response.status === "empty") {
                console.log("No elements to show")
            }
            else if (response.status === "error") {
                console.log(response.error); // this is un unknown error
            }
        } catch (err) { // this is the error relative to the try operation
            throw err;
        }
    }

    const handleSubmit = (event) => {

        event.preventDefault();
        setErrorMessage('');
        setShowAlert(false);

        if (parseQuery()) {
            props.setLoadingList(true);
            search(query);
        };
    };

    return (
        <>
            <Form onSubmit={handleSubmit}>
                {showAlert ? <Alert variant='danger' onClose={() => setShowAlert(false)} dismissible>{errorMessage}</Alert> : ''}
                <h1 className="text-center display-6 mb-4">Type the name of a City</h1>
                <InputGroup className="mb-3">
                    <FormControl
                        placeholder="Search"
                        aria-label="search"
                        onChange={ev => setQuery(ev.target.value)}
                        value={query}
                    />
                </InputGroup>
                <div className="col-md-12 text-center">
                    <Button type="submit">Search</Button>
                </div>
            </Form>
        </>
    )
}

function BoatsList(props) {
    return (
        <>
            <ListGroup>
                <ListGroup.Item active>
                    <Container>
                        <Row>
                            <Col sm="8">Title</Col>
                            <Col sm="4">Price</Col>
                        </Row>
                    </Container>
                </ListGroup.Item>
                {props.boatsList.map((b) =>
                    <BoatsRow
                        key={b.link}
                        title={b.title}
                        price={b.price}
                    />)}
            </ListGroup>
        </>
    )
}

function BoatsRow(props) {
    return(
        <>
            <ListGroup.Item>
                <Container fluid>
                    <Row>
                        <Col sm="8">{props.title}</Col>
                        <Col sm="4">{props.price}</Col>
                    </Row>
                </Container>
            </ListGroup.Item>
        </>
    )
}

export { Searchbar, BoatsList };