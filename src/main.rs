use opencv::{
    Result,
    prelude::*,
    videoio,
    highgui
};

fn main() -> Result<()>{
    
    
    // open the web-camera
    let mut camera = videoio::VideoCapture::new(0, videoio::CAP_ANY)?;

    // open a GUI window
    highgui::named_window("window", highgui::WINDOW_FULLSCREEN)?;

    let mut frame = Mat::default();

    camera.read(&mut frame)?;
    highgui::imshow("window", &frame)?;
    highgui::wait_key(0)?;

    Ok(())
}
