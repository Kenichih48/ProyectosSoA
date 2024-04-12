import React, { Component } from "react";
import '../Styles/indexStyle.css';

class Header extends Component {

    render() {
        return (
            <div className="Header">
                <header>
                    <nav>
                        <ul>
                            <li><a href="/">Home</a></li>
                            <li><a href="/menu">Menu</a></li>
                            <li><a href="/reservation">Reservations</a></li>
                        </ul>
                    </nav>
                </header>
            </div>
        );
    }

}

export default Header;