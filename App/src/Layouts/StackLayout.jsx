import { Outlet } from "react-router-dom";
import "./Styles/StackLayout.css";

const RootLayout = () => {
    return (
        <div id="stackLayout">
            <div className="headerWrap"></div>
            <div className="bodyWrap">
                <Outlet />
            </div>
        </div>
    );
};

export default RootLayout;
