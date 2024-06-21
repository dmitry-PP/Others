import React from "react";
import Main from "./components/Main";
import Order from "./components/Order";

import {BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Basket from "./components/Basket";
import Favourite from "./components/Favourite";
import About from "./components/About";
import Catalog from "./components/Catalog";
import {AppProvider} from "./utils/Context"
import { PageAnimation } from "./utils/Animations";

class App extends React.Component{
    
    render(){
        return(
            <AppProvider>
                <Router>
                    <Routes>
                        <Route path="/" element={<PageAnimation><Main/></PageAnimation>}/>
                        <Route path="/order" element={<PageAnimation><Order/></PageAnimation>}/>
                        <Route path="/basket" element={<PageAnimation><Basket/></PageAnimation>}/>
                        <Route path="/favourite" element={<PageAnimation><Favourite/></PageAnimation>}/>
                        <Route path="/about/:productId" element={<PageAnimation><About/></PageAnimation>}/>
                        <Route path="/catalog" element={<PageAnimation><Catalog/></PageAnimation>}/>
                    </Routes>
                </Router>
            </AppProvider>
        )
    }
}

export default App;
