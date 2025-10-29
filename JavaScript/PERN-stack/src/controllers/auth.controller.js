import {pool} from "../db.js"
import bcrypt from 'bcrypt';
import {createAccesTooken} from "../libs/jwt.js"

export const signin = (req, res) => res.send('ingresando');

export const signup = async (req, res, next) => {
    const { name, email, password } = req.body;
    
    try {
        const hashedPassword = await bcrypt.hash(password, 10);  // ✅ hash, no hashed
        console.log(hashedPassword);

        const result = await pool.query(
            "INSERT INTO usuarios (name, email, password) VALUES ($1, $2, $3) RETURNING *", 
            [name, email, hashedPassword]
        );
        
        const token = await createAccesTooken({id: result.rows[0].id});
        console.log(result);
        
        res.cookie("token", token, {
            httpOnly: true,
            sameSite: "none",
            maxAge: 60 * 60 * 24 * 1000  // 1 day
        });
        
        return res.json(result.rows[0]);
        
    } catch (error) {
        if (error.code === "23505") {
            return res.status(409).json({ message: "El correo ya esta registrado" });
        }
        console.log(error);
        next(error);
    }
};

export const signout = (req, res) => res.send('cerrando sesión');

export const profile = (req, res) => res.send('perfil de usuario');  