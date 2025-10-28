import pg from "pg";

export const pool = new pg.Pool({
port: 5433,
host: "localhost",
user: "postgres",
password: "admin",
database: "PERN",
});

pool.on("connect", () => {
    console.log("conectado a la base de datos");
});




