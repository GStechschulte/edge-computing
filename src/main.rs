use opencv::{
    Result,
    prelude::*,
    videoio,
    highgui,
    imgproc
};

fn main() -> Result<()>{
    
    // open the web-camera
    let mut camera = videoio::VideoCapture::new(0, videoio::CAP_ANY)?;

    // open a GUI window
    highgui::named_window("window", highgui::WINDOW_FULLSCREEN)?;

    let mut frame = Mat::default();

    loop {
        camera.read(&mut frame)?;
        highgui::imshow("window", &frame)?;
        let key = highgui::wait_key(1)?;
        if key == 123 {
            break;
        }
    }

    Ok(())
}
