import React,{useContext,useState,useEffect} from "react";
import Footer from "./Footer";
import Header from "./Header";
import axios from "axios";
import { getMap } from "../utils/Utils";


import "../static/about.css";
import CardSettings from "./CardSettings";
import {AppStateContext} from "../utils/Context"

function Basket(){


    const { appendToBasket,decreaseQuantity,increaseQuantity } = useContext(AppStateContext);
    console.log("local",localStorage.getItem("basket"))
    let basket = getMap(JSON.parse(localStorage.getItem("basket")))

    const [products, setProducts] = useState([])
    const [price,setPrice] = useState(0)
	useEffect(()=> {
		axios.get('http://localhost:3001/products')
		.then(res=>{
			setProducts(res.data.filter(elem=> basket.has(elem.id)))
		    }
		)
		.catch(err=>console.log(err))
		},[localStorage.basket,price])


        return(
			<main>
                <Header Main="" Catalog="" Favourite="" Basket="active" About="" Order=""/>
                <div class="container mt-5">
                    <div class="row">
                        {products.map((elem)=>{
                                return <CardSettings decreaseQuantity={decreaseQuantity} increaseQuantity={increaseQuantity} flagBasket={true} price={elem.price} rmFrom={appendToBasket} Text="Удалить из корзины" id={elem.id} name={elem.name} description={elem.description} image={elem.image}/>
                            })}
                    </div>

                    {    
                    basket.size!=0 && 
                    (<>
                    <div class="text-center" style={{backgroundColor: "#f8f9fa",  padding: 20+'px',  marginTop: 20+'px'}}>
                        <h5>Итого к оплате:</h5>
                        <h3>{products.reduce(
                            (accumulator, currentValue) => accumulator + (+currentValue.price*basket.get(currentValue.id)),
                            0) } руб
                        </h3>
                        <a href="/order" class="btn btn-success">Оформить заказ</a>
                    </div>
                    </>)
                    }
                </div>
                <Footer/>
            </main>
        )
    
}

export default Basket;