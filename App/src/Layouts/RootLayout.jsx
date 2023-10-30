import { Outlet } from "react-router-dom";
import Header from "../Components/Header";
import "./Styles/RootLayout.css";

const RootLayout = () => {
    return (
        <div id="rootLayout">
            <div className="headerWrap">
                <Header />
            </div>
            <div className="bodyWrap">
                <Outlet />
            </div>
        </div>
    );
};

export default RootLayout;
