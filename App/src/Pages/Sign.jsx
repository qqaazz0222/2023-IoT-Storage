import { useNavigate } from "react-router-dom";
import "./Styles/Sign.css";

const Sign = () => {
    const navigate = useNavigate();
    return (
        <div id="sign">
            <div className="body">
                <h1>IoT 저장소</h1>
                <h6>저장소를 사용, 관리, 공유해보세요.</h6>
            </div>
            <div className="footer">
                <div className="btnWrap">
                    <button
                        onClick={() => {
                            navigate("/sign/in");
                        }}
                    >
                        로그인
                    </button>
                </div>
                <button
                    className="linkBtn"
                    onClick={() => {
                        navigate("/sign/up");
                    }}
                >
                    가입하기
                </button>
            </div>
        </div>
    );
};

export default Sign;
