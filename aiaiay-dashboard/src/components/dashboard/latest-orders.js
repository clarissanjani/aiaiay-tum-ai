import { format } from 'date-fns';
import { v4 as uuid } from 'uuid';
import PerfectScrollbar from 'react-perfect-scrollbar';
import {
  Box,
  Button,
  Card,
  CardHeader,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  TableSortLabel,
  Tooltip
} from '@mui/material';
import ArrowRightIcon from '@mui/icons-material/ArrowRight';
import { SeverityPill } from '../severity-pill';

const orders = [
  {
    id: uuid(),
    coordinates: '48.046631,  11.409035',
    detection: 'Forest',
    recommendation: 'No Energy System'
  },
  {
    id: uuid(),
    coordinates: '48.065815, 11.397576',
    detection: 'Pasture',
    recommendation: 'Agrisolar'
  },
  {
    id: uuid(),
    coordinates: '48.217041, 11.732871',
    detection: 'Lake',
    recommendation: 'No Energy System'
  },
  {
    id: uuid(),
    coordinates: '48.224984, 11.546671',
    detection: 'Herbaceous Vegetation',
    recommendation: 'Solar Energy'
  },
  {
    id: uuid(),
    coordinates: '48.116617, 11.865148',
    detection: 'Forest',
    recommendation: 'No Energy System'
  },
  {
    id: uuid(),
    coordinates: '48.233154, 11.501452',
    detection: 'Permanent Crop',
    recommendation: 'Agrisolar'
  },
       {
         id: uuid(),
         coordinates: '48.231045, 11.577201',
         detection: 'Annual Crop',
         recommendation: 'Solar Energy'
       },
       {
         id: uuid(),
         coordinates: '48.150759,11.600224',
         detection: 'River',
         recommendation: 'Hydropower'
       },
       {
         id: uuid(),
         coordinates: '48.156796, 11.571591',
         detection: 'Urban',
         recommendation: 'Solar Energy'
       },
       {
         id: uuid(),
         coordinates: '48.228682, 11.586132',
         detection: 'Highway',
         recommendation: 'No Energy System'
       },
];

export const LatestOrders = (props) => (
  <Card {...props}>
    <CardHeader title="Recommendations on where to place solar and wind energy sites" />
    <PerfectScrollbar>
      <Box sx={{ minWidth: 600 }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>
                Coordinates
              </TableCell>
              <TableCell>
                Detection
              </TableCell>
              <TableCell sortDirection="desc">
                <Tooltip
                  enterDelay={300}
                  title="Sort"
                >
                  <TableSortLabel
                    active
                    direction="desc"
                  >
                    Recommendation
                  </TableSortLabel>
                </Tooltip>
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {orders.map((order) => (
              <TableRow
                hover
                key={order.id}
              >
                <TableCell>
                  {order.coordinates}
                </TableCell>
                <TableCell>
                  {order.detection}
                </TableCell>
                <TableCell>
                  {order.recommendation}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Box>
    </PerfectScrollbar>
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'flex-end',
        p: 2
      }}
    >
      <Button
        color="primary"
        endIcon={<ArrowRightIcon fontSize="small" />}
        size="small"
        variant="text"
      >
        View all
      </Button>
    </Box>
  </Card>
);
