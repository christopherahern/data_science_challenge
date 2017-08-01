"""Class for parsing DICOM files."""
import os
from dicom_server import DicomServer


class DicomParser:
    """Class for parsing DICOM files."""

    def __init__(self, **kwargs):
        """Initialize with url to DICOM server."""
        self.server = DicomServer(**kwargs)

    def get_info(self, patient):
        """Return main DICOM tags from Orthanc."""
        url = os.path.join('patients', patient)
        return self.server.api(url)['MainDicomTags']

    def radiation_total_dose(self, patient_id):
        """Calculate total dose in Gy of treatment plan."""
        # TODO: write method here
        return
