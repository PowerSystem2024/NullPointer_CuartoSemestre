const express = require("express");
const app = express();
const cors = require("cors");
const path = require("path");

const { MercadoPagoConfig, Preference } = require("mercadopago");

const client = new MercadoPagoConfig({ accessToken: "APP_USR-7816407769071637-092400-c7a4013f4c0ddd3183a6ded9503ce811-286501235" });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.use(express.static(path.join(__dirname, "../client")));
app.use(cors());

app.get("/", function (req, res) {
	res.sendFile(path.resolve(__dirname, "..", "client", "index.html"));
});

app.post("/create_preference", async (req, res) => {
	try {
		console.log("Cuerpo de la solicitud recibido:", req.body);
		
		const items = req.body.map(product => ({
			title: product.title,
			unit_price: Number(product.unit_price),
			quantity: Number(product.quantity),
		}));
		
		console.log("Items formateados para Mercado Pago:", items);

		const preference = new Preference(client);
		
		const body = {
			items: items,
			back_urls: {
				"success": "https://http://localhost:8080",
				"failure": "https://www.mercadopago.com.ar/sandbox/failure",
				"pending": "https://www.mercadopago.com.ar/sandbox/pending" 
			},
			auto_return: "approved",
		};

		const response = await preference.create({ body });
		res.json({
			id: response.id
		});
	} catch (error) {
		console.error("Error al crear la preferencia:", error);
		res.status(500).json({ error: "Error al crear la preferencia." });
	}
});

app.get('/feedback', function (req, res) {
	res.json({
		Payment: req.query.payment_id,
		Status: req.query.status,
		MerchantOrder: req.query.merchant_order_id
	});
});

app.listen(8080, () => {
	console.log("The server is now running on Port 8080");
});