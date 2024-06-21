import Footer from "./Footer";
import Header from "./Header";
import React,{ useEffect, useState,useContext } from "react";
import axios from "axios";
import "../static/about.css";
import Card from "./Card";
import { AppStateContext } from "../utils/Context";



function Catalog(){
    const { appendToBasket, appendToFavourites } = useContext(AppStateContext);

    const [products, setProducts] = useState([])
    const [category, setCategory] = useState("")
    const [name, setName] = useState("")

    const search = (data)=>data.filter((elem)=> elem.name.toLowerCase().includes(name.toLowerCase())
    && (category=="" || elem.category == category))

	useEffect(()=> {
		axios.get('http://localhost:3001/products')
		.then(res=>{
			setProducts(search(res.data))
			
		}
		)
		.catch(err=>console.log(err))
		},[name,category])

        return(
			<main>
                <Header Main="" Catalog="active" Favourite="" Basket="" About="" Order=""/>
                <div class="container mt-4">
                    <div class="row">
                        <div class="col-lg-6">
                            <div class="form-inline">
                            <input type="text" class="form-control mb-2 mr-sm-2" id="searchInput" placeholder="Поиск товара"/>
                            <button onClick={(e)=>setName(document.getElementById("searchInput").value)} type="submit" class="btn btn-primary mb-2">Найти</button>
                            </div>
                        </div>
                    </div>

                    <div class="row" style={{marginBottom: 20+'px'}}>
                        <div class="col-lg-6">
                            <select class="form-control" value={category} onChange={(e)=> setCategory(e.currentTarget.value)}>
                                <option value="">Все категории</option>
                                <option value="Чипсы">Чипсы</option>
                                <option value="Конфеты">Конфеты</option>
                                <option value="Напитки">Напитки</option>
                                <option value="Варенье">Варенье</option>
                                <option value="Мороженное">Мороженное</option>
                                <option value="Семьки">Семьки</option>

                            </select>
                        </div>
                    </div>

                    <div class="row">

                    {(products).map((elem)=>{
						return <Card price={elem.price} extra={true} addToFavourite={appendToFavourites} addToBasket={appendToBasket} id={elem.id} name={elem.name} description={elem.description} image={elem.image}/>
					})}	

                   
                    </div>
                </div>

                <Footer/>
            </main>
        )
    
}

export default Catalog;