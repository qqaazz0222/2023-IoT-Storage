import axios from "axios";

import IconFolder from "../Images/IconFolder.png";
import AI from "../Images/ai.png";
import APK from "../Images/apk.png";
import CSS from "../Images/css.png";
import DOC from "../Images/doc.png";
import IMAGE from "../Images/image.png";
import ISO from "../Images/iso.png";
import JS from "../Images/js.png";
import MP3 from "../Images/mp3.png";
import MUSIC from "../Images/music.png";
import OTF from "../Images/otf.png";
import PDF from "../Images/pdf.png";
import PHP from "../Images/php.png";
import PPT from "../Images/ppt.png";
import PSD from "../Images/psd.png";
import SVG from "../Images/svg.png";
import TEXT from "../Images/text.png";
import TTF from "../Images/ttf.png";
import TXT from "../Images/txt.png";
import VECTOR from "../Images/vector.png";
import VIDEO from "../Images/video.png";
import WORD from "../Images/word.png";
import XSLX from "../Images/xslx.png";
import ZIP from "../Images/zip.png";
import TOP from "../Images/top.png";
import "./Styles/FileIcon.css";

const FileIcon = ({ name, ext, chgPath, downFile, goTop }) => {
    let icon;
    switch (ext) {
        case "back":
            icon = TOP;
            break;
        case "":
            icon = IconFolder;
            break;
        case "ai":
            icon = AI;
            break;
        case "apk":
            icon = APK;
            break;
        case "css":
            icon = CSS;
            break;
        case "doc":
            icon = DOC;
            break;
        case "png":
            icon = IMAGE;
            break;
        case "jpg":
            icon = IMAGE;
            break;
        case "jpeg":
            icon = IMAGE;
            break;
        case "iso":
            icon = ISO;
            break;
        case "js":
            icon = JS;
            break;
        case "mp3":
            icon = MP3;
            break;
        case "wav":
            icon = MUSIC;
            break;
        case "otf":
            icon = OTF;
            break;
        case "pdf":
            icon = PDF;
            break;
        case "php":
            icon = PHP;
            break;
        case "ppt":
            icon = PPT;
            break;
        case "psd":
            icon = PSD;
            break;
        case "svg":
            icon = SVG;
            break;
        case "ttf":
            icon = TTF;
            break;
        case "txt":
            icon = TXT;
            break;
        case "vector":
            icon = VECTOR;
            break;
        case "mp4":
            icon = VIDEO;
            break;
        case "word":
            icon = WORD;
            break;
        case "xslx":
            icon = XSLX;
            break;
        case "zip":
            icon = ZIP;
            break;
        default:
            icon = TEXT;
            break;
    }
    return (
        <div
            className="fileIcon"
            title={name}
            onClick={() => {
                if (ext === "back") {
                    goTop();
                } else {
                    if (ext === "") {
                        console.log("CHGPATH");
                        chgPath(name);
                    } else {
                        console.log("DOWNLOAD");
                        downFile(name);
                    }
                }
            }}
        >
            <img src={icon} alt={name} srcset="" />
            <span>{name}</span>
        </div>
    );
};

export default FileIcon;
