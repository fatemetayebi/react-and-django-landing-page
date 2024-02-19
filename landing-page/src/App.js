import "./App.css";
import Home from "./Components/Home"
import About from "./Components/About";
import Products from "./Components/Products";
import Contact from "./Components/Contact";
import Footer from "./Components/Footer";

function App() {
  return (
    <div className="App">
      <Home />
      <About />
      <Products />
      <Contact />
      <Footer />
    </div>
  );
}

export default App;
