const ExifTool = require("exiftool-vendored").ExifTool
const exiftool = new ExifTool({taskTimeoutMillis: 5000})


function print_video_info(filepath) {
    exiftool
        .read(filepath)
        .then((tags) =>
            console.log(tags)
        )
        .catch((err) => console.error("Something terrible happened: ", err))
}

const path = "./halo-kukon.webm"
print_video_info(path)