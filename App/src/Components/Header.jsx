import { useLocation, useNavigate } from "react-router-dom";
import "./Styles/Header.css";
import { useEffect } from "react";

const Header = () => {
    const navigate = useNavigate();
    const location = useLocation();
    return (
        <div id="header">
            <div className="tabWrap">
                <div
                    className={
                        location.pathname === "/summary" ? "tab active" : "tab"
                    }
                    onClick={() => {
                        navigate("/summary");
                    }}
                >
                    요약
                </div>
                <div
                    className={
                        location.pathname === "/storage" ? "tab active" : "tab"
                    }
                    onClick={() => {
                        navigate("/storage");
                    }}
                >
                    저장소 관리
                </div>
                <div
                    className={
                        location.pathname === "/device" ? "tab active" : "tab"
                    }
                    onClick={() => {
                        navigate("/device");
                    }}
                >
                    디바이스 관리
                </div>
                <div
                    className={
                        location.pathname === "/user" ? "tab active" : "tab"
                    }
                    onClick={() => {
                        navigate("/user");
                    }}
                >
                    사용자 관리
                </div>
            </div>
        </div>
    );
};

export default Header;
