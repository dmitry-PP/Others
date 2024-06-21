import React,{ useEffect, useState,useContext,useRef } from "react";
import axios from "axios";

import Header from "./Header";
import Footer from "./Footer";
import Card from "./Card"
import "../static/main.css";
import { AppStateContext } from "../utils/Context";
import emailjs from '@emailjs/browser';
import { useForm } from "react-hook-form";

function randomChoice(arr, count=4) {
	let newArray = new Array();
	let copy = arr.slice();

	for(let i =0; i<count; i++){
		let index = Math.floor(copy.length * Math.random());
		newArray.push(copy[index])
		copy.splice(index, 1);
	}
	
    return newArray;
}


function Main(){
	const form = useRef();
	const {  appendToFavourites } = useContext(AppStateContext);
	const [products, setProducts] = useState([])
	const { register, handleSubmit, formState: { errors } } = useForm();

	useEffect(()=> {
		axios.get('http://localhost:3001/products')
		.then(res=>{
			setProducts(randomChoice(res.data))
		}
		)
		.catch(err=>console.log(err))
		},[])

		const sendEmail = (data) => {
			console.log(data)
			
			
			emailjs.sendForm('service_4i9tkgk', 'template_xmh5mjk', form.current, {
				publicKey: 'TqgphfT3SsUpNHcn6',
			})
			.then(
				() => {
				  alert('Письмо отправлено!');
				},
				(error) => {
					console.log(error)
				  alert('Упс... ВОзникли проблемы с отправкой почты');
				},
			  );}
		

        return(
            <main>
                <Header Main="active" Catalog="" Favourite="" Basket="" About="" Order=""/>
                <content id="content-bd">
				<div class="container mt-4">
					<div class="row">
						<div class="col-md-9">
							<h2>Добро пожаловать в магазин "Зелёный ряд"!</h2>
							<p class="desc">Здесь вы найдете всё, что нужно для здорового питания и не только.</p>
						</div>
					</div>

					<div id="productList" class="row mt-4">
						<div class="col-md-12">
							<h3>Наш ассортимент</h3>
						</div>

					{(products).map((elem)=>{
						return <Card price={elem.price} extra={false} addTo={appendToFavourites} id={elem.id} name={elem.name} description={elem.description} image={elem.image}/>
					})}	
					
						
					</div>
				</div>
				<div class="container mt-4 mb-4">
					<div class="card">
					<div class="card-body">
						<h5 class="card-title">Обратная связь</h5>
						<form ref={form} onSubmit={handleSubmit(sendEmail)}>
            <div className="form-group">
                <label htmlFor="name">Имя</label>
                <input
                    type="text"
                    className="form-control"
                    id="name"
                    placeholder="Введите ваше имя"
                    {...register("name", { required: true })}
                />
                {errors.name && <span className="text-danger">Это поле обязательно</span>}
            </div>
            <div className="form-group">
                <label htmlFor="email">Email</label>
                <input
                    type="email"
                    className="form-control"
                    id="email"
                    placeholder="Введите ваш email"
                    {...register("email", { required: true, pattern: /^\S+@\S+$/i })}
                />
                {errors.email && <span className="text-danger">Введите корректный email</span>}
            </div>
            <div className="form-group">
                <label htmlFor="message">Сообщение</label>
                <textarea
                    className="form-control"
                    id="message"
                    rows="3"
                    placeholder="Введите ваше сообщение"
                    {...register("message", { required: true })}
                ></textarea>
                {errors.message && <span className="text-danger">Это поле обязательно</span>}
            </div>
            <button type="submit" className="btn btn-primary">Отправить</button>
        </form>
					</div>
					</div>
				</div>
			</content>
                <Footer/>
            </main>
        )
    
}

export default Main;