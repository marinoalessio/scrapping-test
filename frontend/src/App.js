import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Navbar, Row, Col, Spinner } from 'react-bootstrap';
import { useState } from 'react';
import './App.css';
import { Searchbar, BoatsList } from './Components';

function App() {

  const [boatsList, setBoatsList] = useState([]);
  const [loadingList, setLoadingList] = useState(false);
  
  // here if query is not empty, and not loading, show if there is no result

  return (
    <>
      <BoatsNavbar />
      <Container >
        <Row className="justify-content-md-center mt-4">
          <Col lg={6}>
            <Searchbar setBoatsList={setBoatsList} setLoadingList={setLoadingList} />
          </Col>
        </Row>
        <Row className="justify-content-md-center mt-4">
          <Col lg={6}>


            {loadingList ?
              <Spinner animation="border" /> :
              <BoatsList boatsList={boatsList} loadingList={loadingList} />
            }
          </Col>

        </Row>

      </Container>
    </>
  );
}

function BoatsNavbar() {
  return (
    <Navbar bg="dark" variant="dark">
      <Container>
        <Navbar.Brand href="#home">Boats Scraper</Navbar.Brand>

      </Container>
    </Navbar>
  );
}

export default App;
