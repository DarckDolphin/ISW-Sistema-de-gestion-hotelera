import React from "react"
import { Route, Routes } from "react-router-dom"
import Dashboard from "../pages/dashboard"
import { RoutesNotFound } from "../RoutesNotFound/RoutesNotFound"
import Reservas from "../pages/reservas"


export const PrivateRouter = () => {
  return (
    <RoutesNotFound>
      <Route path="/" element={<Dashboard/>} />
      <Route path="/dashboard" element={<Dashboard/>} />
      <Route path="/reservas" element={<Reservas/>} />
      <Route path="/user" element={<Dashboard/>} />
    </RoutesNotFound>    
  )
}