import React from 'react'
import { NavLink } from 'react-router-dom'

function Home() {
  return (
    <div>

        <NavLink to="/">home</NavLink>
        <br />
        <br />
        <NavLink to="/three">three</NavLink>
    </div>
  )
}

export default Home