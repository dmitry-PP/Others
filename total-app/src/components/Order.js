import React,{useRef,useState,useEffect} from "react";
import { useForm } from "react-hook-form";
import Header from "./Header";
import Footer from "./Footer";
import "../static/about.css";
import emailjs from '@emailjs/browser';
import axios from "axios";
import { getMap } from "../utils/Utils";
import Captcha from "../utils/Captcha"


function Order() {
    const { register, handleSubmit, formState: { errors } } = useForm();
    const [captchaValid, setCaptchaValid] = useState(false);

    let basket = getMap(JSON.parse(localStorage.getItem("basket")))

    const form = useRef();
    const onSubmit = (data) => {
        console.log(data)
            if(basket.size==0){
                alert("В вашей корзине нет товаров!!!")
                return
            }

            if (!captchaValid) {
                alert('Заполните каптчу!!!');
                return;
              }

			emailjs.sendForm('service_4i9tkgk', 'template_07z1pnd', form.current, {
				publicKey: 'TqgphfT3SsUpNHcn6',
			})
			.then(
				() => {
				  alert('Письмо отправлено!');
				},
				(error) => {
				  alert('Упс...');
                  console.log(error)
				},
			  );}

    const [products, setProducts] = useState([])
	useEffect(()=> {
		axios.get('http://localhost:3001/products')
		.then(res=>{
			setProducts(res.data.filter(elem=> basket.has(elem.id)))
		    }
		)},[localStorage.basket])
        


    return (
        <main>
            <Header Main="" Catalog="" Favourite="" Basket="" About="" Order="active"/>
            <content>
                <div className="container mt-5">
                    <div className="row justify-content-center">
                        <div className="col-lg-8">
                            <h2 className="mb-4">Оформление заказа</h2>
                            <form id="orderForm" ref={form} onSubmit={handleSubmit(onSubmit)}>
                                <div className="form-group">
                                    <label htmlFor="fullName">ФИО</label>
                                    <input type="text" className="form-control" id="fullName" name="fullName" {...register("fullName", { required: true })} />
                                    {errors.fullName && <span className="text-danger">Это поле обязательно</span>}
                                </div>
                                <div className="form-group">
                                    <label htmlFor="address">Адрес доставки</label>
                                    <input type="text" className="form-control" id="address" name="address" {...register("address", { required: true })} />
                                    {errors.address && <span className="text-danger">Это поле обязательно</span>}
                                </div>
                                <div className="form-group">
                                    <label htmlFor="paymentMethod">Способ оплаты</label>
                                    <select className="form-control" id="paymentMethod" name="paymentMethod" {...register("paymentMethod", { required: true })}>
                                        <option value="">Выберите способ оплаты</option>
                                        <option value="Наличными">Наличными</option>
                                        <option value="Картой">Картой</option>
                                    </select>
                                    {errors.paymentMethod && <span className="text-danger">Выберите способ оплаты</span>}
                                </div>
                                <div className="form-group">
                                    <textarea hidden id="message" name="message" value={products.map((elem=>{
                                        return `${elem.name} - ${elem.price} * ${basket.get(elem.id)}`
                                    })).join("\n")} {...register("message", { required: false })}/>
                                </div>
                                <Captcha onCaptchaChange={setCaptchaValid} />

                                <button type="submit" className="btn btn-primary" style={{marginTop:15+'px'}}>Отправить заказ</button>
                            </form>
                        </div>
                    </div>
                </div>
            </content>
            <Footer/>
        </main>
    );
}

export default Order;