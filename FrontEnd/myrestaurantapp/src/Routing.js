import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import IndexPage from "./Scripts/indexpage";
import MenuPage from "./Scripts/menupage";
import ReservPage from "./Scripts/reservpage";

export const Routing = ()    => {

    return (
        
        <Router>
            <Routes>
                <Route path="/" element={<IndexPage></IndexPage>} />
                <Route path="/menu" element={<MenuPage></MenuPage>} />
                <Route path="/reservation" element={<ReservPage></ReservPage>} />
            </Routes>
        </Router>
    );

};