import { useNavigate } from "react-router-dom";
import "./Styles/Sign.css";

const Sign = () => {
    const navigate = useNavigate();
    return (
        <div id="sign">
            <div className="body">
                <h1>IoT 저장소</h1>
                <h6>할 일을 작성, 계획, 관리하세요.</h6>
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
