import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatList from './HatList';
import HatForm from './HatForm';
// import ShoesList from './ShoesList';
import ShoesForm from './ShoesForm';

function App(props) {
  // if (props.hats === undefined) {
  //   return null;
  // }
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="hats">
            <Route index element={<HatList hats={props.hats}/>} />
            {/* <Route path="new" element={<HatForm />} /> */}
          </Route> 
          {/* <Route path="shoe" element={<ShoesList shoes={shoe} />} /> */}
          <Route path="shoe/new" element={<ShoesForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
export default App;
